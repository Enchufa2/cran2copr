%global packname  SPOT
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}
Summary:          Sequential Parameter Optimization Toolbox

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-ggplot2 

%description
A set of tools for model based optimization and tuning of algorithms. It
includes surrogate models, optimizers and design of experiment approaches.
The main interface is spot, which uses sequentially updated surrogate
models for the purpose of efficient optimization. The main goal is to ease
the burden of objective function evaluations, when a single evaluation
requires a significant amount of resources.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/consoleCallTrialScript.R
%{rlibdir}/%{packname}/INDEX
