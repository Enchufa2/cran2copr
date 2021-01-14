%global packname  sass
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Syntactically Awesome Style Sheets ('Sass')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 

%description
An 'SCSS' compiler, powered by the 'LibSass' library. With this, R
developers can use variables, inheritance, and functions to generate
dynamic style sheets. The package uses the 'Sass CSS' extension language,
which is stable, powerful, and CSS compatible.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
