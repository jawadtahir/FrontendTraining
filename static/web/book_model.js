/**
 * Created by jawad on 5/9/17.
 */
var Author = Backbone.Model.extend({
    default: {
        dateofbirth: ''
    }

});
var Name = Backbone.Model.extend({
    default: {
        salutation: '',
        first_name: '',
        last_name: ''
    }
});
var Contact = Backbone.Model.extend({
    default: {
        contact_method: '',
        country_code: 0,
        contact_number: 0,
        author: 0,
        publisher: 0
    }
});
var Publisher = Backbone.Model.extend({
    default: {
        country: '',
        website: ''
    }
});

Author.validate = function (attributes) {
    if (!attributes.name) {
        return 'Name is missing'
    }
    if (!attributes.dateofbirth) {
        return 'Date of birth os missing'
    }
};

Name.validate = function (attributes) {
    if (!attributes.first_name) {
        return 'Invalid name'
    }
    if (!attributes.last_name) {
        return 'Invalid name'
    }
};

Publisher.validate = function (attributes) {
    if (!attributes.country) {
        return 'Invalid country'
    }
};

Contact.validate = function (attributes) {
    if (!attributes.author && !attributes.publisher) {
        return 'Contact number must be associated with person'
    }
};