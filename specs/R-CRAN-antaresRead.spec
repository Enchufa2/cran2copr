%global packname  antaresRead
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}
Summary:          Import, Manipulate and Explore the Results of an 'Antares'Simulation

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-lubridate >= 1.7.1
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-lubridate >= 1.7.1
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 

%description
Import, manipulate and explore results generated by 'Antares', a powerful
open source software developed by RTE (Réseau de Transport d’Électricité)
to simulate and study electric power systems (more information about
'Antares' here :
<https://github.com/AntaresSimulatorTeam/Antares_Simulator>). You can see
the results of several ANTARES studies here :
<http://bpnumerique.rte-france.com/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/format_output
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/vignetteData
%{rlibdir}/%{packname}/INDEX
