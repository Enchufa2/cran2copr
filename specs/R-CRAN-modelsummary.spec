%global packname  modelsummary
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Summary Tables and Plots for Statistical Models and Data: Beautiful, Customizable, and Publication-Ready

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kableExtra >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tables 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-kableExtra >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tables 
Requires:         R-CRAN-tibble 

%description
Create beautiful and customizable tables to summarize several statistical
models side-by-side. Draw coefficient plots, multi-level cross-tabs,
dataset summaries, balance tables (a.k.a. "Table 1s"), and correlation
matrices. This package supports dozens of statistical models, and it can
produce tables in HTML, LaTeX, Word, Markdown, PDF, PowerPoint, Excel,
RTF, JPG, or PNG. Tables can easily be embedded in 'Rmarkdown' or 'knitr'
dynamic documents.

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
