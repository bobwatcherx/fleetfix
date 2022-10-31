from math import pi
import flet
from Appbar.appbar import appbar
from flet import IconButton,View,TemplateRoute,ElevatedButton,Container,animation,transform,Column,AppBar,Text,colors,Page,Row,TextField,icons

def main(page:Page):
	page.title = "ini main"
	page.vertical_alignment = "center"

	txt_number = TextField(value="0",text_align="right",width=100)
	nama = "aplikasi ku"
	c = Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=transform.Rotate(0, alignment="center"),
        animate_rotation=animation.Animation(duration=300, curve="bounceOut"),
    )

	def kurang(e):
		txt_number.value = int(txt_number.value) - 1
		page.update()
	def tambah(e):
		txt_number.value = int(txt_number.value) + 1
		page.update()
	def ganti(e):
		nama = "tolol"
		page.update()
	def animate(e):
		c.rotate.angle += pi / 2
		page.update()
	
	troute = TemplateRoute(page.route)
	if troute.match("/store/:id"):
		print("Book view ID:", troute.id)
	else:
		print("Unknown route")
	
	def tololajing(e):
		if not namamu.value:
			namamu.error_text = "isi dulu tolol"
			page.update()
		else:
			name = namamu.value
			page.clean()
			page.add(Text(f"hasilnya,{name}"))
	
	def route_change(route):
		page.views.clear()
		page.views.append(
			View(
				"/",
				[
				AppBar(title=Text("Home")),
				Column(
					[
					Text(page.route),

					ElevatedButton(
						"ini home",
						on_click=page.go("/store/""ewqeq")
						)
					],
					alignment="center"

					)

				]
			)
			)
		if page.route == "/store/:id":
			page.views.append(
			View(
				"/store/:id",
				[
				AppBar(title=Text("store")),
				Column(
					[
		Text(page.route),

					ElevatedButton(
						"ini store",
						on_click=view_pop
						)
					],
					alignment="center"

					)

				]
			)
			)
		page.add(Text(f"New route: {route}"))
		page.update()
	def go_route(e):
		page.route="/store"
		page.update()
	def view_pop(view):
		page.views.pop()
		backbtn = page.views[-1]
		page.go(backbtn.route)
	namamu = TextField(label="tolol")
	page.on_route_change = route_change
	page.on_view_pop = view_pop
	page.go(page.route)
	page.add(
		appbar,
		Text(page.route),
		Column(
			[
			namamu,
			ElevatedButton(
				"goblok",
				on_click=go_route
				),
			ElevatedButton(
				"saya",
				on_click=animate
				),
			c,
				Row(
					[
						IconButton(icons.ADD,on_click=kurang),
						Text("tolol",size=30,color="red",weight="w500"),
						IconButton(icons.REMOVE,on_click=tambah),

					],
					alignment="center"
					)

			]
			)
		)
flet.app(target=main,view=flet.WEB_BROWSER)

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")