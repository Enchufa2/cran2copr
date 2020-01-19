%global packname  smacof
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Multidimensional Scaling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-candisc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-plotrix 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-nnls 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-candisc 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Implements the following approaches for multidimensional scaling (MDS)
based on stress minimization using majorization (smacof):
ratio/interval/ordinal/spline MDS on symmetric dissimilarity matrices, MDS
with external constraints on the configuration, individual differences
scaling (idioscal, indscal), MDS with spherical restrictions, and
ratio/interval/ordinal/spline unfolding (circular restrictions,
row-conditional). Various tools and extensions like jackknife MDS,
bootstrap MDS, permutation tests, MDS biplots, gravity models,
unidimensional scaling, drift vectors (asymmetric MDS), classical scaling,
and Procrustes are implemented as well.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/NEWSRd2txt.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs