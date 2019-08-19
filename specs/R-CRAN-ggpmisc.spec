%global packname  ggpmisc
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Miscellaneous Extensions to 'ggplot2'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.1
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-zoo >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-polynom >= 1.3.9
BuildRequires:    R-CRAN-splus2R >= 1.2.2
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-broom >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-xts >= 0.11.2
BuildRequires:    R-grid 
Requires:         R-MASS >= 7.3.51.1
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-zoo >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-polynom >= 1.3.9
Requires:         R-CRAN-splus2R >= 1.2.2
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-broom >= 0.5.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-xts >= 0.11.2
Requires:         R-grid 

%description
Extensions to 'ggplot2' respecting the grammar of graphics paradigm.
Specialization of method ggplot(): accept and convert on the fly time
series data. Geom: "table", "plot" and "grob" add insets to plots using
native data coordinates, while "table_npc", "plot_npc" and "grob_npc" do
the same using "npc" coordinates through new aesthetics "npcx" and "npcy".
Statistics: locate and tag peaks and valleys; count observations in
different quadrants of a plot; select observations based on 2D density;
label with the equation of a polynomial fitted with lm() or other types of
models; labels with P-value, R^2 or adjusted R^2 or information criteria
for fitted models; label with ANOVA table for fitted models; label with
summary for fitted models. Model fit classes for which suitable methods
are provided by package 'broom' are supported.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX