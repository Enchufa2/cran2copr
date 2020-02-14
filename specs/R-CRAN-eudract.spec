%global packname  eudract
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Creates Safety Results Summary in XML to Upload to EudraCT

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xslt 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xslt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-xml2 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
The remit of the European Clinical Trials Data Base (EudraCT
<https://eudract.ema.europa.eu/> ) is to provide open access to summaries
of all registered clinical trial results; thus aiming to prevent
non-reporting of negative results and provide open-access to results to
inform future research. The amount of information required and the format
of the results, however, imposes a large extra workload at the end of
studies on clinical trial units. In particular, the
adverse-event-reporting component requires entering: each unique
combination of treatment group and safety event; for every such event
above, a further 4 pieces of information (body system, number of
occurrences, number of subjects, number exposed) for non-serious events,
plus an extra three pieces of data for serious adverse events (numbers of
causally related events, deaths, causally related deaths). This package
prepares the required statistics needed by EudraCT and formats them into
the precise requirements to directly upload an XML file into the web
portal, with no further data entry by hand.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
