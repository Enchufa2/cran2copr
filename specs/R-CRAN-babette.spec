%global packname  babette
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Control 'BEAST2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.3
BuildRequires:    R-CRAN-beastier >= 2.1
BuildRequires:    R-CRAN-mauricer 
BuildRequires:    R-CRAN-tracerer 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-beautier >= 2.3
Requires:         R-CRAN-beastier >= 2.1
Requires:         R-CRAN-mauricer 
Requires:         R-CRAN-tracerer 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-xml2 

%description
'BEAST2' (<http://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAST2' is
commonly accompanied by 'BEAUti 2', 'Tracer' and 'DensiTree'. 'babette'
provides for an alternative workflow of using all these tools separately.
This allows doing complex Bayesian phylogenetics easily and reproducibly
from 'R'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX