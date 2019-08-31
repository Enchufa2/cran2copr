%global packname  ape
%global packver   5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3
Release:          1%{?dist}
Summary:          Analyses of Phylogenetics and Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-nlme 
BuildRequires:    R-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-nlme 
Requires:         R-lattice 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-parallel 

%description
Functions for reading, writing, plotting, and manipulating phylogenetic
trees, analyses of comparative data in a phylogenetic framework, ancestral
character analyses, analyses of diversification and macroevolution,
computing distances from DNA sequences, reading and writing nucleotide
sequences as well as importing from BioConductor, and several tools such
as Mantel's test, generalized skyline plots, graphical exploration of
phylogenetic data (alex, trex, kronoviz), estimation of absolute
evolutionary rates and clock-like trees using mean path lengths and
penalized likelihood, dating trees with non-contemporaneous sequences,
translating DNA into AA sequences, and assessing sequence alignments.
Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
triangle methods, and several methods handling incomplete distance
matrices (NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some
functions call external applications (PhyML, Clustal, T-Coffee, Muscle)
whose results are returned into R.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs