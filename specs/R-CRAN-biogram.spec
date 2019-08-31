%global packname  biogram
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          N-Gram Analysis of Biological Sequences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-partitions 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-partitions 

%description
Tools for extraction and analysis of various n-grams (k-mers) derived from
biological sequences (proteins or nucleic acids). Contains QuiPT (quick
permutation test) for fast feature-filtering of the n-gram data.

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
%{rlibdir}/%{packname}/INDEX