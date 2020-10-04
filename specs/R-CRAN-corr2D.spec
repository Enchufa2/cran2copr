%global packname  corr2D
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of 2D Correlation Analysis in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 8.2
BuildRequires:    R-parallel >= 3.0.2
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-grDevices >= 3.0.2
BuildRequires:    R-graphics >= 3.0.2
BuildRequires:    R-utils >= 3.0.2
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-mmand >= 1.3.0
BuildRequires:    R-CRAN-colorspace >= 1.3.0
BuildRequires:    R-CRAN-doParallel >= 1.0.8
BuildRequires:    R-CRAN-rgl >= 0.93.996.1
BuildRequires:    R-CRAN-profr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-fields >= 8.2
Requires:         R-parallel >= 3.0.2
Requires:         R-stats >= 3.0.2
Requires:         R-grDevices >= 3.0.2
Requires:         R-graphics >= 3.0.2
Requires:         R-utils >= 3.0.2
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-mmand >= 1.3.0
Requires:         R-CRAN-colorspace >= 1.3.0
Requires:         R-CRAN-doParallel >= 1.0.8
Requires:         R-CRAN-rgl >= 0.93.996.1
Requires:         R-CRAN-profr 
Requires:         R-CRAN-xtable 

%description
Implementation of two-dimensional (2D) correlation analysis based on the
Fourier-transformation approach described by Isao Noda (I. Noda (1993)
<DOI:10.1366/0003702934067694>). Additionally there are two plot functions
for the resulting correlation matrix: The first one creates colored 2D
plots, while the second one generates 3D plots.

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
%{rlibdir}/%{packname}/INDEX
