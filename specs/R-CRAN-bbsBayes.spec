%global packname  bbsBayes
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Hierarchical Bayesian Analysis of North American BBS Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-jagsUI 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-geofacet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-jagsUI 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-geofacet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-tools 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-rappdirs 

%description
The North American Breeding Bird Survey (BBS) is a long-running program
that seeks to monitor the status and trends of the breeding birds in North
America. Since its start in 1966, the BBS has accumulated over 50 years of
data for over 300 species of North American Birds. Given the temporal and
spatial structure of the data, hierarchical Bayesian models are used to
assess the status and trends of these 300+ species of birds. 'bbsBayes'
allows you to perform hierarchical Bayesian analysis of BBS data. You can
run a full model analysis for one or more species that you choose, or you
can take more control and specify how the data should be stratified,
prepared for 'JAGS', or modelled. The functions provided here allow you to
replicate analyses performed by the United State Geological Survey (USGS,
see Link and Sauer (2011) <doi:10.1525/auk.2010.09220>) and Canadian
Wildlife Service (CWS, see Smith and Edwards (2020)
<doi:10.1101/2020.03.26.010215>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/area-weight
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/composite-regions
%{rlibdir}/%{packname}/data-import
%{rlibdir}/%{packname}/data-terms
%doc %{rlibdir}/%{packname}/geofacet-grids
%doc %{rlibdir}/%{packname}/maps
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
