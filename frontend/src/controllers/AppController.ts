import { IEventParam, Metadata, Singleton } from '@zeedhi/core';
import { Menu, MenuButton } from '@zeedhi/common';

@Singleton
export class AppController {
  public toggleMenu({ component }: IEventParam<MenuButton>) {
    const menu = Metadata.getInstance<Menu>(component.menuName);
    menu.toggleMenu();
    if (menu.opened && !menu.miniState) {
      if (menu.showSearch) {
        setTimeout(() => {
          const searchInput = document.querySelector('.zd-menu-search-input input');
          if (searchInput) (searchInput as any).focus();
        }, 100);
      } else {
        const firstMenuItem = document.querySelector('.zd-menu-link, .zd-menu-group > div');
        if (firstMenuItem) (firstMenuItem as any).focus();
      }
    }
  }
}
