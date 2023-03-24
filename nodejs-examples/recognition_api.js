try {
    console.log(require.resolve('nopecha'));
} catch(e) {
    console.log('\n');
    console.log('The Nopecha library is not installed.');
    console.log('Please install using the following command:');
    console.log('npm i nopecha');
    console.log('\n');
    process.exit(e.code);
}


const NOPECHA_API_KEY = "YOUR KEY HERE";

const { Configuration, NopeCHAApi, AuthenticationError } = require('nopecha');
const configuration = new Configuration({
    apiKey: NOPECHA_API_KEY,
});
const nopecha = new NopeCHAApi(configuration);

(async () => {
    try {
        // solve an hcaptcha recognition challenge
        const clicks = await nopecha.solveRecognition({
            type: 'hcaptcha',
            task: 'Please click each image containing a cat-shaped cookie.',
            image_urls: Array.from({length: 9}, (_, i) => `https://nopecha.com/image/demo/hcaptcha/${i}.png`),
        });

        // print the grids to click
        console.log(clicks);
    } catch (e) {
        if (e instanceof AuthenticationError) {
            console.log('\n')
            console.log(`You have provided an invalid key: ${NOPECHA_API_KEY}`, '\n')
            console.log('Please set NOPECHA_API_KEY with your NopeCHA key.')
            console.log('Visit https://nopecha.com/manage to view your keys.')
            console.log('Or join our official Discord for instructions on acquiring test keys.')
            console.log('https://nopecha.com/discord')
            console.log('\n')
        }
        else {
            throw e;
        }
    }
})();
