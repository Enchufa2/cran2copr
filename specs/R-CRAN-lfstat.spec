%global packname  lfstat
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Low Flow Statistics for Daily Stream Flow Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-lmomRFA 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lmom 
Requires:         R-lattice 
Requires:         R-CRAN-lmomRFA 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-plyr 

%description
The "Manual on Low-flow Estimation and Prediction", published by the World
Meteorological Organisation (WMO), gives a comprehensive summary on how to
analyse stream flow data focusing on low-flows. This packages provides
functions to compute the described statistics and produces plots similar
to the ones in the manual.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/samplesheets
%{rlibdir}/%{packname}/INDEX
