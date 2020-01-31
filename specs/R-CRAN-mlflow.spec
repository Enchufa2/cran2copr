%global packname  mlflow
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Interface to 'MLflow'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-forge 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-swagger 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-forge 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-swagger 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zeallot 
Requires:         R-CRAN-glue 

%description
R interface to 'MLflow', open source platform for the complete machine
learning life cycle, see <https://mlflow.org/>. This package supports
installing 'MLflow', tracking experiments, creating and running projects,
and saving and serving models.

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
%{rlibdir}/%{packname}/INDEX
