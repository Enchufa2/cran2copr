%global packname  googleCloudRunner
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          R Scripts in the Google Cloud via Cloud Run, Cloud Build andCloud Scheduler

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-openssl >= 1.4.1
BuildRequires:    R-CRAN-googleAuthR >= 1.1.1
BuildRequires:    R-CRAN-googleCloudStorageR >= 0.5.1
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-yaml >= 2.2.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-openssl >= 1.4.1
Requires:         R-CRAN-googleAuthR >= 1.1.1
Requires:         R-CRAN-googleCloudStorageR >= 0.5.1
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to easily enable R scripts in the Google Cloud Platform. Utilise
cloud services such as Cloud Run <https://cloud.run> for R over HTTP,
Cloud Build <https://cloud.google.com/cloud-build/> for Continuous
Delivery and Integration services and Cloud Scheduler
<https://cloud.google.com/scheduler/> for scheduled scripts.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cloudbuild
%doc %{rlibdir}/%{packname}/docker
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/polygot
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/schedule
%doc %{rlibdir}/%{packname}/scheduled_rmarkdown
%doc %{rlibdir}/%{packname}/ssh
%{rlibdir}/%{packname}/INDEX