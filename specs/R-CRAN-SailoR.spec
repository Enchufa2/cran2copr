%global packname  SailoR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Extension of the Taylor Diagram to Two-Dimensional Vector Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
A new diagram for the verification of vector variables (wind, current,
etc) generated by multiple models against a set of observations is
presented in this package. It has been designed as a generalization of the
Taylor diagram to two dimensional quantities. It is based on the analysis
of the two-dimensional structure of the mean squared error matrix between
model and observations. The matrix is divided into the part corresponding
to the relative rotation and the bias of the empirical orthogonal
functions of the data. The full set of diagnostics produced by the
analysis of the errors between model and observational vector datasets
comprises the errors in the means, the analysis of the total variance of
both datasets, the rotation matrix corresponding to the principal
components in observation and model, the angle of rotation of
model-derived empirical orthogonal functions respect to the ones from
observations, the standard deviation of model and observations, the root
mean squared error between both datasets and the squared two-dimensional
correlation coefficient. See the output of function UVError() in this
package.

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
