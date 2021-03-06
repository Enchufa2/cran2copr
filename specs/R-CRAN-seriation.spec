%global packname  seriation
%global packver   1.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Ordering Objects Using Seriation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-qap 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-registry 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-qap 
Requires:         R-cluster 
Requires:         R-CRAN-gclus 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-colorspace 
Requires:         R-MASS 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-registry 

%description
Infrastructure for ordering objects with an implementation of several
seriation/sequencing/ordination techniques to reorder matrices,
dissimilarity matrices, and dendrograms. Also provides (optimally)
reordered heatmaps, color images and clustering visualizations like
dissimilarity plots, and visual assessment of cluster tendency plots (VAT
and iVAT). Hahsler et al (2008) <doi:10.18637/jss.v025.i03>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
