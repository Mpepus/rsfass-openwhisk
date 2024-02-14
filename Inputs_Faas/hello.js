/**
 * Hello world as an OpenWhisk action.
 */
function main(params) {
   return {payload:  'Hello, ' + params.name + ' from ' + params.place};
}
