import random
import sys
from time import sleep
from settings import Settings
import pygame
from pygame import mixer
from ship import Ship
from bullet import Bullet, AlienBullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvaders:
    """General class intended for manage the resources and the way the game works"""

    def __init__(self):
        """Initialize the game and it's resources"""
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invaders")

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.ship = Ship(self)
        self.ships = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self._create_fleet()
        self._load_sound_effects()

        self.play_button = Button(self, "New Game")

    def run_game(self):
        """Run the game loop"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullets()
                self.random_alien_bullets()
                
            self._update_screen()

    def _check_events(self):
        """Reaction for events generated by keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game after clicking 'Play' button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.alien_bullets.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.settings.initialize_dynamic_settings()
            self.scoreboard.prep_score()
            self.scoreboard.prep_lvl()
            self.scoreboard.prep_ships()

    def _check_keydown_events(self, event):
        """Reactions for inserted key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.laser_fx.play()

    def _check_keyup_events(self, event):
        """Reactions for released key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _load_sound_effects(self):
        self.explosion_fx = pygame.mixer.Sound("audio/explosion.wav")
        self.explosion_fx.set_volume(0.25)

        self.explosion2_fx = pygame.mixer.Sound("audio/explosion2.wav")
        self.explosion2_fx.set_volume(0.25)

        self.laser_fx = pygame.mixer.Sound("audio/laser.wav")
        self.laser_fx.set_volume(0.1)

    def _fire_bullet(self):
        """Create a new bullet and add it to a bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet's location and remove those which are beyond the screen"""
        self.bullets.update()
        self._check_bullet_alien_collisions()

        # Delete bullets which are beyond the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def random_alien_bullets(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.settings.last_alien_shot > self.settings.alien_bullet_cd:
            self.shooting_alien = random.choice(self.aliens.sprites())
            alien_bullet = AlienBullet(self, self.shooting_alien)
            self.alien_bullets.add(alien_bullet)
            self.settings.last_alien_shot = time_now

    def _update_alien_bullets(self):
        """Update alien bullet's location and remove those which are beyond the screen"""
        self.alien_bullets.update()
        self._check_alien_bullet_ship_collisions()

        # Delete bullets which are beyond the screen
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top > self.settings.screen_height:
                self.alien_bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """Check collisions between bullet and alien"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.explosion2_fx.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.alien_bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            sleep(0.5)

            self.stats.level += 1
            self.scoreboard.prep_lvl()

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create full alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Get amount of rows of aliens
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (10 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Check if fleet is near the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move fleet one row down and change its moving direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_bullet_ship_collisions(self):
        """Check collisions between alien bullet and ship"""
        collision = pygame.sprite.spritecollideany(self.ship, self.alien_bullets)

        if collision:
            self.explosion_fx.play()
            self._ship_hit()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """Reaction for hit the ship by alien"""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            self.bullets.empty()
            self.alien_bullets.empty()
            self.ship.center_ship()
            sleep(1)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check, if any alien get to the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on screen and get into new screen"""

        # Refreshing the screen during every game loop
        self.screen.blit(self.settings.bg, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for alien_bullet in self.alien_bullets.sprites():
            alien_bullet.draw_alien_bullet()

        self.aliens.draw(self.screen)
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display the last modified screen
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvaders()
    ai.run_game()
