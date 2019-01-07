import {NbMenuItem} from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
    {
        title: 'IoT Dashboard',
        icon: 'nb-home',
        link: '/pages/iot-dashboard',
        home: true,
    },
    {
        title: 'Network',
        icon: 'nb-shuffle',
        children: [
            {
                title: 'Grapher',
                link: '/pages/networkGrapher',
            },
            {
                title: 'Log Parser',
                link: '/pages/logParser',
            },
        ],
    },
    {
        title: 'Setting',
        icon: 'nb-gear',
        children: [
            {
                title: 'Users',
                link: '/pages/networkGrapher',
            },
            {
                title: 'Health',
                link: '/pages/networkGrapher',
            },
            {
                title: 'Login History',
                link: '/pages/networkGrapher',
            },
        ],
    },
];
