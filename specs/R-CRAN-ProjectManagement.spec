%global packname  ProjectManagement
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Management of Deterministic and Stochastic Projects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-kappalab 
BuildRequires:    R-CRAN-GameTheory 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-kappalab 
Requires:         R-CRAN-GameTheory 
Requires:         R-CRAN-lpSolveAPI 

%description
Management problems of deterministic and stochastic projects. It obtains
the duration of a project and the appropriate slack for each activity in a
deterministic context. In addition it obtains a schedule of activities'
time (Castro, Gómez & Tejada (2007) <doi:10.1016/j.orl.2007.01.003>). It
also allows the management of resources. When the project is done, and the
actual duration for each activity is known, then it can know how long the
project is delayed and make a fair delivery of the delay between each
activity (Bergantiños, Valencia-Toledo & Vidal-Puga (2018)
<doi:10.1016/j.dam.2017.08.012>). In a stochastic context it can estimate
the average duration of the project and plot the density of this duration,
as well as, the density of the early and last times of the chosen
activities. As in the deterministic case, it can make a distribution of
the delay generated by observing the project already carried out.

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
