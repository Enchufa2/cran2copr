%global packname  picante
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}
Summary:          Integrating Phylogenies and Ecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-nlme 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-nlme 
Requires:         R-methods 

%description
Functions for phylocom integration, community analyses, null-models,
traits and evolution. Implements numerous ecophylogenetic approaches
including measures of community phylogenetic and trait diversity,
phylogenetic signal, estimation of trait values for unobserved taxa, null
models for community and phylogeny randomizations, and utility functions
for data input/output and phylogeny plotting. A full description of
package functionality and methods are provided by Kembel et al. (2010)
<doi:10.1093/bioinformatics/btq166>.

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
%{rlibdir}/%{packname}/libs