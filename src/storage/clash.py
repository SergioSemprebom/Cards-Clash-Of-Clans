import flet as ft

def main(page :ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #alinhamento vertical
    page.window_min_with = 500 #largura minima da janela
    page.bgcolor = ft.colors.BLACK #cor de fundo

    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.colors.SURFACE],
        ),
        content=ft.Image(
            src='https://static.wikia.nocookie.net/clashofclans/images/9/9b/Barbarian-xx.png/revision/latest?cb=20170703143506',
            scale=ft.Scale(scale=1.6)
        )
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4', color=ft.colors.ORANGE),
                ft.Text(
                    value='Bárbaro Semprebom',
                    weight=ft.FontWeight.BOLD,
                    size=20,
                    color=ft.colors.BLACK,

                ),
                ft.Text(
                    value='O Bárbaro é um guerreiro escocês vestido de kilt com uma expressão raivosa e pronta para a batalha, faminto por destruição. Ele tem bigode de ferradura amarelo assassino.', 
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                    
                ),
            ]
        )
    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(

                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='20',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),

                ft.VerticalDivider(opacity=0.6),
                ft.Column(

                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='16',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='VELOCIDADE',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                ft.VerticalDivider(opacity=0.6),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='152',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE,
                        )
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        height = 650,
        width = 400,
        shadow=ft.BoxShadow(blur_radius=100,color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,# Sombra no box
        border_radius=ft.border_radius.all(30),# Arredondamento do box
        bgcolor=ft.colors.WHITE,
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
