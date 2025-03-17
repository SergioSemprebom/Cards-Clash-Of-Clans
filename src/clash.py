import flet as ft

def main(page :ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #alinhamento vertical
    page.window_min_with = 500 #largura minima da janela
    page.bgcolor = ft.Colors.BLACK #cor de fundo

    image = ft.Container(
        expand=2,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.Colors.SURFACE],
        ),
        content=ft.Image(
            src='https://e7.pngegg.com/pngimages/78/567/png-clipart-clash-of-clans-warrior-illustration-clash-of-clans-clash-royale-goblin-barbarian-game-clash-of-clans-video-game-fictional-character-thumbnail.png',
        )
    )
    info = ft.Container()
    skills = ft.Container()

    layout = ft.Container(
        height = 400,
        width = 400,
        shadow=ft.BoxShadow(blur_radius=100,color=ft.Colors.BROWN),# Sombra no box
        border_radius=ft.border_radius.all(30),# Arredoamento do box
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    )

    page.add(layout)
    #page.update() NAO PRECISA DESSA LINHA, POIS O page.add já esta fazendo isso

if __name__ == '__main__':
    ft.app(target=main)
