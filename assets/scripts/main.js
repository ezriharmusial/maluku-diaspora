// import external dependencies
import 'jquery';

// Import everything from autoload
import "./autoload/**/*"

// import local dependencies
import Router from './util/Router';
import common from './routes/common';
import adresdetails from './routes/adresdetails';
import adresform from './routes/adresform';
import adreslijst from './routes/adreslijst';

/** Populate Router instance with DOM routes */
const routes = new Router({
  // All pages
  common,
  // Adres details
  adresdetails,
  // Adres forms
  adresform,
  // Home page
  adreslijst,
});

// Load Events
jQuery(document).ready(() => routes.loadEvents());
