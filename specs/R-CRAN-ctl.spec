%global packname  ctl
%global packver   1.0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          1%{?dist}
Summary:          Correlated Trait Locus (CTL) Mapping in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-qtl 
Requires:         R-MASS 
Requires:         R-CRAN-qtl 

%description
Analysis of genetical genomic data to identify genetic loci associated
with correlation changes in quantitative traits (CTL).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README.txt
%doc %{rlibdir}/%{packname}/STATUS.txt
%doc %{rlibdir}/%{packname}/TODO.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs