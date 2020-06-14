%global packname  shinyMobile
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Mobile Ready 'shiny' Apps with Standalone Capabilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 

%description
Develop outstanding 'shiny' apps for 'iOS', 'Android', desktop as well as
beautiful 'shiny' gadgets. 'shinyMobile' is built on top of the latest
'Framework7' template <https://framework7.io>. Discover 14 new input
widgets (sliders, vertical sliders, stepper, grouped action buttons,
toggles, picker, smart select, ...), 2 themes (light and dark), 12 new
widgets (expandable cards, badges, chips, timelines, gauges, progress
bars, ...) combined with the power of server-side notifications such as
alerts, modals, toasts, action sheets, sheets (and more) as well as 3
layouts (single, tabs and split).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/framework7-5.1.3
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
