%global packname  nimble
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          MCMC, Particle Filtering, and Programmable Hierarchical Modeling

License:          BSD_3_clause + file LICENSE | GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-R6 

%description
A system for writing hierarchical statistical models largely compatible
with 'BUGS' and 'JAGS', writing nimbleFunctions to operate models and do
basic R-style math, and compiling both models and nimbleFunctions via
custom-generated C++.  'NIMBLE' includes default methods for MCMC,
particle filtering, Monte Carlo Expectation Maximization, and some other
tools.  The nimbleFunction system makes it easy to do things like
implement new MCMC samplers from R, customize the assignment of samplers
to different parts of a model from R, and compile the new samplers
automatically via C++ alongside the samplers 'NIMBLE' provides.  'NIMBLE'
extends the 'BUGS'/'JAGS' language by making it extensible: New
distributions and functions can be added, including as calls to external
compiled code.  Although most people think of MCMC as the main goal of the
'BUGS'/'JAGS' language for writing models, one can use 'NIMBLE' for
writing arbitrary other kinds of model-generic algorithms as well.  A full
User Manual is available at <https://r-nimble.org>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/classic-bugs
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/CppCode
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/make
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
