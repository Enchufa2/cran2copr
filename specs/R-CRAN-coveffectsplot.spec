%global packname  coveffectsplot
%global packver   0.0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Produce Forest Plots to Visualize Covariate Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-table1 
Requires:         R-utils 

%description
Produce forest plots to visualize covariate effects using either the
command line or an interactive 'Shiny' application.

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
