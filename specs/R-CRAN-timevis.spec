%global packname  timevis
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Timeline Visualizations in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 

%description
Create rich and fully interactive timeline visualizations. Timelines can
be included in Shiny apps and R markdown documents, or viewed from the R
console and 'RStudio' Viewer. 'timevis' includes an extensive API to
manipulate a timeline after creation, and supports getting data out of the
visualization into R. Based on the 'vis.js' Timeline module and the
'htmlwidgets' R package.

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
