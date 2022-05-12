import { Prop, Component } from 'vue-property-decorator';
import { ZdComponent } from '@zeedhi/vuetify';
import { ImgLink as ImgLinkClass } from './common/ImgLink';

/**
 * DocTable component
 */
@Component
export default class ImgLink extends ZdComponent {
  @Prop({ type: String, default: '' }) public to!: string;

  @Prop({ type: String, default: '' }) public src!: string;

  public instance!: ImgLinkClass;

  public instanceType: typeof ImgLinkClass = ImgLinkClass;
}
