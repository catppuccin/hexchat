<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://hexchat.github.io/">HexChat</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/aszecsei/hexchat/stargazers"><img src="https://img.shields.io/github/stars/aszecsei/hexchat?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/aszecsei/hexchat/issues"><img src="https://img.shields.io/github/issues/aszecsei/hexchat?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/aszecsei/hexchat/contributors"><img src="https://img.shields.io/github/contributors/aszecsei/hexchat?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="assets/sample.webp"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="assets/latte.png"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/frappe.png"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/macchiato.png"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mocha.png"/>
</details>

## Usage

1. Clone this repository locally
2. Run the installation script while HexChat is closed:
```sh
./install 'latte' # or frappe, macchiato, mocha 
```
3. Launch HexChat

Alternatively, for manual installation:

2. Copy the desired `colors.conf` file to `$XDG_CONFIG_HOME/hexchat/` (usually this is `~/.config/hexchat`)
	- For example: `cp frappe/colors.conf ~/.config/hexchat/colors.conf`

## 🙋 FAQ
-   Q: **_"Why doesn't all of HexChat match the theme?"_**\
	A: HexChat themes only affect the panel backgrounds and text colors; to get the rest of the window to match you'll also need the [GTK](https://github.com/catppuccin/gtk) theme.
-	Q: **_"Why isn't this working with flatpak?"_**\
	A: Try copying the `colors.conf` file to `~/.var/app/io.github.Hexchat/config/hexchat/` instead.

## 💝 Thanks to

- [aszecsei](https://github.com/aszecsei)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
