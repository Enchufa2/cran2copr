%global packname  rdhs
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          3%{?dist}%{?buildtag}
Summary:          API Client and Dataset Management for the Demographic and HealthSurvey (DHS) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-storr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-iotools 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-foreign 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-storr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-iotools 

%description
Provides a client for (1) querying the DHS API for survey indicators and
metadata (<https://api.dhsprogram.com/#/index.html>), (2) identifying
surveys and datasets for analysis, (3) downloading survey datasets from
the DHS website, (4) loading datasets and associate metadata into R, and
(5) extracting variables and combining datasets for pooled analysis.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
