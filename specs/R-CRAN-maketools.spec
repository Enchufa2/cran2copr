%global packname  maketools
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploring and Testing the Toolchain and System Libraries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sys >= 3.1
Requires:         R-CRAN-sys >= 3.1

%description
A collection of helper functions that interface with the appropriate
system utilities to learn about the build environment. Lets you explore
'make' rules to test the local configuration, or query 'pkg-config' to
find compiler flags and libs needed for building packages with external
dependencies. Also contains tools to analyze which libraries that a
installed R package linked to by inspecting output from 'ldd' in
combination with information from your distribution package manager, e.g.
'rpm' or 'dpkg'. Finally the package provides Windows-specific utilities
to automatically find or install the suitable version of the 'Rtools'
build environment, and diagnose some common problems.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
