%global packname  qtlhot
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Inference for QTL Hotspots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-stats 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-mnormt 
Requires:         R-utils 
Requires:         R-CRAN-corpcor 

%description
Functions to infer co-mapping trait hotspots and causal models. Chaibub
Neto E, Keller MP, Broman AF, Attie AD, Jansen RC, Broman KW, Yandell BS
(2012) Quantile-based permutation thresholds for QTL hotspots. Genetics
191 : 1355-1365. <doi:10.1534/genetics.112.139451>. Chaibub Neto E, Broman
AT, Keller MP, Attie AD, Zhang B, Zhu J, Yandell BS (2013) Modeling
causality for pairs of phenotypes in system genetics. Genetics 193 :
1003-1013. <doi:10.1534/genetics.112.147124>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/deprecated.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/notes
%doc %{rlibdir}/%{packname}/parallel
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs