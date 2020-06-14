%global packname  otuSummary
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Summarizing OTU Table Regarding the Composition, Abundance andBeta Diversity of Abundant and Rare Biospheres

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.0.7
BuildRequires:    R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-vegan >= 2.0.7
Requires:         R-CRAN-reshape2 >= 1.4

%description
Summarizes the taxonomic composition, diversity contribution of the rare
and abundant community by using OTU (operational taxonomic unit) table
which was generated by analyzing pipeline of 'QIIME' or 'mothur'. The rare
biosphere in this package is subset by the relative abundance threshold
(for details about rare biosphere please see Lynch and Neufeld (2015)
<doi:10.1038/nrmicro3400>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
