%global packname  stagedtrees
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Staged Event Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Creates and fits staged event tree probability models. Staged event trees
are probabilistic graphical models capable of representing asymmetric
conditional independence statements among categorical variables. This
package contains functions to create, plot and fit staged event trees from
data, moreover different structure learning algorithms are available.
References: Collazo R. A., Görgen C. and Smith J. Q. (2018,
ISBN:9781498729604). Görgen C., Bigatti A., Riccomagno E. and Smith J. Q.
(2018) <arXiv:1705.09457>. Thwaites P. A., Smith, J. Q. (2017)
<arXiv:1510.00186>. Barclay L. M., Hutton J. L. and Smith J. Q. (2013)
<doi:10.1016/j.ijar.2013.05.006>. Smith J. Q. and Anderson P. E. (2008)
<doi:10.1016/j.artint.2007.05.004>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
