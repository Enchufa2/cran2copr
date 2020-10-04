%global packname  sbioPN
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          sbioPN: Simulation of deterministic and stochastic spatialbiochemical reaction networks using Petri Nets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
sbioPN is a package suited to perform simulation of deterministic and
stochastic systems of biochemical reaction networks with spatial effects.
Models are defined using a subset of Petri Nets, in a way that is close at
how chemical reactions are defined. For deterministic solutions, sbioPN
creates the associated system of differential equations "on the fly", and
solves it with a Runge Kutta Dormand Prince 45 explicit algorithm. For
stochastic solutions, sbioPN offers two variants of Gillespie algorithm,
or SSA. For hybrid deterministic/stochastic, it employs the Haseltine and
Rawlings algorithm, that partitions the system in fast and slow reactions.
sbioPN algorithms are developed in C to achieve adequate performance.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
