%global packname  RcmdrPlugin.pointG
%global packver   0.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.6
Release:          3%{?dist}%{?buildtag}
Summary:          Graphical POINT of view for questionnaire data Rcmdr Plug-In

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-tcltk 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-RColorBrewer 

%description
This package provides a Rcmdr "plug-in" to analyze questionnaire data.

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
