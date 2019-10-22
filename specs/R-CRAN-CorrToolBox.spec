%global packname  CorrToolBox
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Modeling Correlational Magnitude Transformations inDiscretization Contexts

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BinNonNor 
BuildRequires:    R-CRAN-BinOrdNonNor 
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-BinNonNor 
Requires:         R-CRAN-BinOrdNonNor 
Requires:         R-CRAN-GenOrd 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 

%description
Modeling the correlation transitions under specified distributional
assumptions within the realm of discretization in the context of the
latency and threshold concepts. The details of the method are explained in
Demirtas, H. and Vardar-Acar, C. (2017) <DOI:10.1007/978-981-10-3307-0_4>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
