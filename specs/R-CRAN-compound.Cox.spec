%global packname  compound.Cox
%global packver   3.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.18
Release:          1%{?dist}
Summary:          Univariate Feature Selection and Compound Covariate forPredicting Survival

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-survival 
Requires:         R-CRAN-numDeriv 
Requires:         R-survival 

%description
Univariate feature selection and compound covariate methods under the Cox
model with high-dimensional features (e.g., gene expressions). Available
are survival data for non-small-cell lung cancer patients with gene
expressions (Chen et al 2007 New Engl J Med) <DOI:10.1056/NEJMoa060096>,
statistical methods in Emura et al (2012 PLoS ONE)
<DOI:10.1371/journal.pone.0047627>, Emura & Chen (2016 Stat Methods Med
Res) <DOI:10.1177/0962280214533378>, and Emura et al.
(2019)<DOI:10.1016/j.cmpb.2018.10.020>. Algorithms for generating
correlated gene expressions are also available.

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
%{rlibdir}/%{packname}/INDEX