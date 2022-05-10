odoo.define("inb_pe_pos_sunat_search_ruc.models", function (require) {
  "use strict";
  var models = require("point_of_sale.models");
  models.load_fields("res.partner",["l10n_latam_identification_type_id"]);
  console.log(models.load_fields("res.partner",["l10n_latam_identification_type_id"]));
  models.load_models([
    {
      model: "l10n_latam.identification.type",
      fields: ["id","display_name"],
      loaded: function (self, identification_type) {
          console.log('identification_type');
          console.log(identification_type);
          self.identification_type = identification_type;
      },
    },
  ]);
  models.load_models([
    {
      model: "res.partner.category",
      fields: [],
      loaded: function (self, res_category) {
          console.log('res_category');
        self.res_category = res_category;
      },
    },
  ]);
  models.load_models([
    {
      model: "l10n_pe.res.city.district",
      fields: ["id","display_name","city_id"],
      loaded: function (self, res_district) {
        self.res_district = res_district;
        console.log('res_district');
        console.log(res_district);
      },
    },
  ]);
});