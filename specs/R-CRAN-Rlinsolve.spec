%global packname  Rlinsolve
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Iterative Solvers for (Sparse) Linear System of Equations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-bigmemory 
Requires:         R-Matrix 
Requires:         R-CRAN-Rdpack 

%description
Solving a system of linear equations is one of the most fundamental
computational problems for many fields of mathematical studies, such as
regression problems from statistics or numerical partial differential
equations. We provide basic stationary iterative solvers such as Jacobi,
Gauss-Seidel, Successive Over-Relaxation and SSOR methods. Nonstationary,
also known as Krylov subspace methods are also provided. Sparse matrix
computation is also supported in that solving large and sparse linear
systems can be manageable using 'Matrix' package along with
'RcppArmadillo'. For a more detailed description, see a book by Saad
(2003) <doi:10.1137/1.9780898718003>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs