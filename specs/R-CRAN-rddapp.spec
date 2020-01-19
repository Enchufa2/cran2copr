%global packname  rddapp
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Regression Discontinuity Design Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.6.0
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-AER >= 1.2.5
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-lmtest >= 0.9.35
BuildRequires:    R-CRAN-shiny >= 0.14
Requires:         R-CRAN-R.utils >= 2.6.0
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-AER >= 1.2.5
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-lmtest >= 0.9.35
Requires:         R-CRAN-shiny >= 0.14

%description
Estimation of both single- and multiple-assignment Regression
Discontinuity Designs (RDDs). Provides both parametric (global) and
non-parametric (local) estimation choices for both sharp and fuzzy
designs, along with power analysis and assumption checks. Introductions to
the underlying logic and analysis of RDDs are in Thistlethwaite, D. L.,
Campbell, D. T. (1960) <doi:10.1037/h0044319> and Lee, D. S., Lemieux, T.
(2010) <doi:10.1257/jel.48.2.281>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shinyrdd
%{rlibdir}/%{packname}/INDEX