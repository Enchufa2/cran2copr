%global packname  ROI.plugin.scs
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'SCS' Plug-in for the 'R' Optimization Infrastructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-scs >= 1.3.2
BuildRequires:    R-CRAN-ROI >= 0.3.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-slam 
Requires:         R-CRAN-scs >= 1.3.2
Requires:         R-CRAN-ROI >= 0.3.2
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-slam 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package with the
'SCS' solver for solving convex cone problems.

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
