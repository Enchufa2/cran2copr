%global packname  Bchron
%global packver   4.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.0
Release:          1%{?dist}
Summary:          Radiocarbon Dating, Age-Depth Modelling, Relative Sea Level RateEstimation, and Non-Parametric Phase Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mclust 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mclust 

%description
Enables quick calibration of radiocarbon dates under various calibration
curves (including user generated ones); age-depth modelling as per the
algorithm of Haslett and Parnell (2008)
<DOI:10.1111/j.1467-9876.2008.00623.x>; Relative sea level rate estimation
incorporating time uncertainty in polynomial regression models (Parnell
and Gehrels 2015) <DOI:10.1002/9781118452547.ch32>; non-parametric phase
modelling via Gaussian mixtures as a means to determine the activity of a
site (and as an alternative to the Oxcal function SUM; currently
unpublished), and reverse calibration of dates from calibrated into
un-calibrated years (also unpublished).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs