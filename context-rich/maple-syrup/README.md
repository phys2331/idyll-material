# Maple Syrup

This is an (in-progress) adaptation of the "Maple Syrup Problem", which deals with mass spectroscopy.
It has been adapted both for web use and to focus on aspects dealing with electricity and magnetism.

## Accessing Online

This page will be available at https://phys2331.github.io/idyll-material/maple-syrup/build/index.html.

## Running Locally

- Make sure you have `idyll` installed (`npm i -g idyll`).
- Clone this repo and run `npm install`.
- You can now use the `idyll` command to view this locally in your browser.

## Deploying

Run `idyll build`. The output will appear in the top-level `build` folder. To change the output location, change the `output` option in `package.json`.

Make sure your post has been built, then deploy the build folder via any static hosting service.  Note that if "build" is in the .gitignore you may want to remove it.

## Dependencies

You can install custom dependencies by running `npm install <package-name> --save`. Note that any collaborators will also need download the package locally by running `npm install` after pulling the changes.

Current Dependencies list:
- IdyllApparatusComponent (package name is `idyll-apparatus-component`)
