%global packname  wikisourcer
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Download Public Domain Works from Wikisource

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 

%description
Download public domain works from Wikisource <https://wikisource.org/>, a
free library from the Wikimedia Foundation project.

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
