%global packname  shipunov
%global packver   1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions from Alexey Shipunov

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PBSmapping 
Requires:         R-CRAN-PBSmapping 

%description
A collection of functions for data manipulation, plotting and statistical
computing, to use separately or with the book "Visual Statistics. Use R!":
Shipunov (2020) <http://ashipunov.info/shipunov/software/r/r-en.htm>. Most
useful functions: Bclust(), Jclust() and BootA() which bootstrap
hierarchical clustering; Recode() which does multiple recoding in a fast,
simple and flexible way; Misclass() which outputs confusion matrix even if
classes are not concerted; Overlap() which measures group separation on
any projection; Biarrows() which converts any scatterplot into biplot; and
Pleiad() which is fast and flexible correlogram.

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
