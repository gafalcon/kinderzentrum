var Configuration = {
  Debug: {
    Enabled: true,
    Suggestions: [
      {
        id: 1,
        name: 'Chris Evans'
      },
      {
        id: 2,
        name: 'Robert Downey Jr.'
      },
      {
        id: 3,
        name: 'Chris Hemsworth'
      },
      {
        id: 4,
        name: 'Mark Ruffalo'
      },
      {
        id: 5,
        name: 'Jeremy Renner'
      }
    ],
    PaymentInformation: {
      id: 1,
      payments: [
        {
          patient: 3,
          name: 'Language Therapy',
          observation: 'Adele',
          cost: 20.59,
          date: 11
        },
        {
          patient: 1,
          name: 'Psychotherapy',
          observation: 'Brendon',
          cost: 40.54,
          date: 14
        },
        {
          patient: 2,
          name: 'Physician Therapy',
          observation: 'Liam',
          cost: 10.54,
          date: 9
        },
        {
          patient: 3,
          name: 'Eye Therapy',
          observation: 'Kymberly',
          cost: 15.26,
          date: 12
        }
      ]
    },
    Delay: function (x) {
      return new Promise(function (resolve, reject) {
        setTimeout(function () {
          resolve(x);
        }, 2000);
      });
    }
  },
  Suggestions: {
    Limit: 5
  }
};

var State = {
  CurrentPacient: null
}

function getPatientSuggestionsByNameFragment(nameFragment) {
  var handlePatientSuggestionsPromise;
  if (Configuration.Debug.Enabled) {
    handlePatientSuggestionsPromise = Promise.resolve(Configuration.Debug.Suggestions)
      .then(function (unfilteredSuggestions) {
        return unfilteredSuggestions
          .filter(function (suggestion) {
            return suggestion.name.indexOf(nameFragment) !== -1;
          });
      })
      .then(Configuration.Debug.Delay);
  } else {
    var URL = API.host = '/pacientes?limit=' + Configuration.Suggestions.Limit || 5;
    if (nameFragment !== '') {
      URL += '/query=' + nameFragment;
    }
    handlePatientSuggestionsPromise = fetch(URL)
      .then(function (response) {
        if (response.ok) {
          return response;
        } else {
          var error = new Error(response.statusText);
          error.response = response;
          throw error;
        }
      }).then(function (json) {
        return json.suggestions;
      })
  }
  handlePatientSuggestionsPromise
    .then(function (suggestions) {
      updatePatientSuggestionsDropdown(suggestions);
    })
    .catch(function (error) {
      console.log('Error: ' + error);
      updatePatientSuggestionsDropdown([]);
    });
}

function updatePatientSuggestionsDropdown(suggestions) {
  console.log(suggestions);
}

function getPatientPaymentInformation(id, date) {
  var handlePatientInformationPromise;
  if (Configuration.Debug.Enabled) {
    handlePatientInformationPromise = Promise.resolve({id: id, information: Configuration.Debug.PaymentInformation})
      .then(function (data) {
        return {
          id: data.information.id,
          payments: data.information.payments.filter(function (payment) {
            return payment.patient === data.id && payment.date >= date.from && payment.date <= date.to;
          })
        };
      })
      .then(Configuration.Debug.Delay);
  } else {
    var URL = API.host = '/pagos/payments/' + id + '?from=' + date.from + '&to=' + date.to;
    handlePatientInformationPromise = fetch(URL)
      .then(function (response) {
        if (response.ok) {
          return response;
        } else {
          var error = new Error(response.statusText);
          error.response = response;
          throw error;
        }
      }).then(function (json) {
        return json.information;
      });
  }
  handlePatientInformationPromise
    .then(function (paymentInformation) {
      updatePatientPaymentInformationTable(paymentInformation);
    })
    .catch(function (error) {
      console.log('Error: ' + error);
      updatePatientPaymentInformationTable({});
    });
}

function updatePatientPaymentInformationTable(paymentInformation) {
  console.log(paymentInformation);
}

var API = {
  host: 'http://localhost',
  getPatientSuggestionsByNameFragment: getPatientSuggestionsByNameFragment,
  getPatientPaymentInformation: getPatientPaymentInformation
};