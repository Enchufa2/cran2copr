%global packname  WVPlots
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Common Plots for Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-wrapr >= 2.0.2
BuildRequires:    R-CRAN-rquery >= 1.4.5
BuildRequires:    R-CRAN-rqdatatable >= 1.2.8
BuildRequires:    R-CRAN-cdata >= 1.1.8
BuildRequires:    R-CRAN-sigr >= 1.1.2
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-wrapr >= 2.0.2
Requires:         R-CRAN-rquery >= 1.4.5
Requires:         R-CRAN-rqdatatable >= 1.2.8
Requires:         R-CRAN-cdata >= 1.1.8
Requires:         R-CRAN-sigr >= 1.1.2
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 

%description
Select data analysis plots, under a standardized calling interface
implemented on top of 'ggplot2' and 'plotly'. Plots of interest include:
'ROC', gain curve, scatter plot with marginal distributions, conditioned
scatter plot with marginal densities, box and stem with matching
theoretical distribution, and density with matching theoretical
distribution.

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
